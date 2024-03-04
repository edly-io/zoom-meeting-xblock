/* Javascript for ZoomMeetingXBlock. */
function ZoomMeetingXBlock(runtime, element, config) {
  const client = ZoomMtgEmbedded.createClient();

  function startMeeting() {
    var meetingSDKElement = getOrCreateMeetingDiv();
    client
      .init({
        zoomAppRoot: meetingSDKElement,
        language: config.language,
        patchJsMedia: true,
      })
      .then(() => {
        client.join({
          signature: config.signature,
          sdkKey: config.sdk_key,
          meetingNumber: config.meeting_number,
          password: config.password,
          userName: config.username,
          userEmail: config.user_email,
          tk: config.registrant_token,
          zak: config.zak_token,
        });
      })
      .catch((error) => {
        displayError(error);
      });
  }

  function displayError(error) {
    if (error && typeof error === "object" && "reason" in error) {
        $('#zoomError').append(`<p style="color: red; text-align: center;">Error: ${error.reason}</p>`);
    } else if (typeof error === "string") {
        $('#zoomError').append(`<p style="color: red; text-align: center;">Error: ${error}</p>`);
    }
}

  function getOrCreateMeetingDiv() {
    var meetingSDKElement = $("#meetingSDKElement");

    if (!meetingSDKElement.length) {
        meetingSDKElement = $("<div></div>");
        meetingSDKElement.attr("id", "meetingSDKElement");
        $("body").append(meetingSDKElement);
    }
    console.log('zxaa ', meetingSDKElement)
    return meetingSDKElement[0];
}


  $("#startZoomMeetingId").click(function (eventObject) {
    $(this).hide();
    startMeeting();
  });

  $(function ($) {
    if ("error" in config) {
      $("#startZoomMeetingId").hide();
      displayError(config.error);
    }
  });
}
