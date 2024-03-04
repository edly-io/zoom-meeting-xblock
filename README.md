# zoom-meeting-xblock

Introducing Zoom Meeting Component XBlock, integrating Zoom meeting functionalities directly into the course environment. This enhancement enables users to easily participate in Zoom meetings from within their learning platform.

# Setup

### Install Xblock

```
pip install -e zoom_xblock
```

### **Update  Settings of LMS and CMS**
Add the following Zoom credentials through Studio.
```
SDK KEY OR CLIENT ID
SDK SECRET OR CLIENT SECRET
ZOOM MEETING ID
ZOOM SECURITY PASSCODE
```

### Update Advanced Settings of course


Update the course advanced settings by adding `zoom_xblock` to the list of advanced settings.

## Usage

Publish the XBlock from Studio, and then start the Zoom meeting from the LMS.



