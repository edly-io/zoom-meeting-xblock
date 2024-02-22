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
        client.join({
          signature: config.signature,
          sdkKey: config.sdk_key,
          meetingNumber: config.meeting_number,
          password: config.password,
          userName: config.user_name,
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
    var errorDiv = document.createElement("div");

    if (error && typeof error === "object" && "reason" in error) {
      const reason = error.reason;
      errorDiv.innerHTML = `<p style="color: red; text-align: center;">Error: ${reason}</p>`;
    } else if (typeof error === "string") {
      errorDiv.innerHTML = `<p style="color: red; text-align: center;">Error: ${error}</p>`;
    }
    document.body.appendChild(errorDiv);
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
