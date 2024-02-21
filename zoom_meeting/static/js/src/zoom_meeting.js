/* Javascript for ZoomMeetingXBlock. */
function ZoomMeetingXBlock(runtime, element, config) {
  const client = ZoomMtgEmbedded.createClient();

  function startMeeting() {
    var meetingSDKElement = getOrCreateMeetingDiv();
    client
      .init({
        zoomAppRoot: meetingSDKElement,
        language: "en-US",
        patchJsMedia: true,
      })
      .then(() => {
        client
          .join({
            signature: config.signature,
            sdkKey: config.sdk_key,
            meetingNumber: config.meeting_number,
            password: config.password,
            userName: config.user_name,
            userEmail: config.user_email,
            tk: config.registrant_token,
            zak: config.zak_token,
          })
          .then(() => {
            console.log("Joined Meeting Successfully");
          })
          .catch((error) => {
            console.log(error);
          });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  function getOrCreateMeetingDiv() {
    var meetingSDKElement = document.getElementById("meetingSDKElement");

    if (!meetingSDKElement) {
      meetingSDKElement = document.createElement("div");
      meetingSDKElement.setAttribute("id", "meetingSDKElement");
      document.body.appendChild(meetingSDKElement);
    }

    return meetingSDKElement;
  }

  $("#startZoomMeetingId").click(function (eventObject) {
    $(this).hide();
    startMeeting();
  });

  $(function ($) {
    /* Here's where you'd do things on page load. */
  });
}
