"""Zoom Meeting component XBlock."""

import logging
import time

import jwt
import pkg_resources
from django.conf import settings

from web_fragments.fragment import Fragment
from xblock.completable import CompletableXBlockMixin
from xblock.core import XBlock
from xblock.fields import Scope, String
from xblockutils.studio_editable import StudioEditableXBlockMixin

log = logging.getLogger(__name__)

TOKEN_EXPIRE_TIME = 60 * 60 * 3


def _(text): return text


@XBlock.wants("user")
@XBlock.wants('i18n')
class ZoomMeetingXBlock(XBlock, StudioEditableXBlockMixin, CompletableXBlockMixin):
    """
    Zoom Meeting component XBlock.
    """

    sdk_key = String(
        display_name=_('SDK KEY OR CLIENT ID'),
        default=None,
        scope=Scope.settings,
        help=_("Zoom sdk key OR Client Id"),
    )
    sdk_secret = String(
        display_name=_('SDK SECRET OR CLIENT SECRET'),
        default=None,
        scope=Scope.settings,
        help=_("Zoom sdk Secret OR Client Secret"),
    )

    meeting_number = String(
        display_name=_('ZOOM MEETING NUMBER'),
        default=None,
        scope=Scope.settings,
        help=_("Zoom meeting number"),
    )
    meeting_password = String(
        display_name=_('ZOOM SECURITY PASSCODE'),
        default=None,
        scope=Scope.settings,
        help=_("Zoom security passcode"),
    )
    editable_fields = ['sdk_key', 'sdk_secret', 'meeting_number', 'meeting_password']
    has_author_view = True

    def get_congfiurations(self):
        """
        The `get_configurations` function returns a dictionary with Zoom meeting details and user
        information, including the user's name.

        Returns:
            string: The `get_congfiurations` method returns a dictionary.
        """

        if not all([self.sdk_key, self.sdk_secret, self.meeting_number, self.meeting_password]):
            return {"error": "Configuration value(s) missing."}

        current_user = self.runtime.service(self, "user").get_current_user()
        username = current_user.opt_attrs.get("edx-platform.username")
        language = current_user.opt_attrs.get(
            "edx-platform.user_preferences").get("pref-lang", "en-US")

        return {
            "signature": self.generate_zoom_jwt_signature(),
            "sdk_key": self.sdk_key,
            "meeting_number": self.meeting_number,
            "password": self.meeting_password,
            "username": username,
            "user_email": "",
            "registrant_token": "",
            "zak_token": "",
            "language": language,
        }

    def generate_zoom_jwt_signature(self):
        """generate zoom jwt signature

        Returns:
            string: jwt token
        """
        iat = int(time.time()) - 30
        exp = iat + TOKEN_EXPIRE_TIME
        role = 1 if self.runtime.user_is_staff else 0
        payload = {
            "sdkKey": self.sdk_key,
            "mn": self.meeting_number,
            "role": role,
            "iat": iat,
            "exp": exp,
            "appKey": self.sdk_key,
            "tokenExp": exp,
        }
        token = jwt.encode(
            payload,
            self.sdk_secret,
            algorithm=settings.JWT_AUTH.get("JWT_ALGORITHM", "HS256"),
        )
        return token.decode("utf-8") if isinstance(token, bytes) else token

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the ZoomMeetingXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/zoom_meeting.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/zoom_meeting.css"))

        js_urls = [
            "public/lib/react.min.js",
            "public/lib/react-dom.min.js",
            "public/lib/redux.min.js",
            "public/lib/redux-thunk.min.js",
            "public/lib/lodash.min.js",
            "public/lib/zoom-meeting-embedded-3.1.6.min.js",
        ]

        for js_url in js_urls:
            frag.add_javascript_url(self.runtime.local_resource_url(self, js_url))

        frag.add_javascript(self.resource_string("static/js/src/zoom_meeting.js"))
        frag.initialize_js("ZoomMeetingXBlock", self.get_congfiurations())
        return frag

    def author_view(self, context=None):
        """
        Render a static message to join a meeting from the LMS.
        """
        html = self.resource_string("static/html/zoom_meeting_studio.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/zoom_meeting.css"))
        return frag

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ZoomMeetingXBlock",
             """<zoom_meeting/>
             """),
            ("Multiple ZoomMeetingXBlock",
             """<vertical_demo>
                <zoom_meeting/>
                <zoom_meeting/>
                <zoom_meeting/>
                </vertical_demo>
             """),
        ]
