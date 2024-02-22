# zoom-meeting-xblock

Introducing Zoom Meeting Component XBlock, integrating Zoom meeting functionalities directly into the course environment. This enhancement enables users to easily participate in Zoom meetings from within their learning platform.

# Setup

### Install Xblock

```
pip install -e zoom_xblock
```

### **Update  Settings of LMS and CMS**
Add the following values in the lms and cms configuration file
```python
ZOOM_MEETING_SDK_KEY: 'zoom-sdk-key or zoom-client-id'
ZOOM_MEETING_SDK_SECRET: 'zoom-sdk-secret or zoom-client-secret'
ZOOM_MEETING_NUMBER: 'zoom-meeting-id'
ZOOM_SECURITY_PASSCODE: 'zoom-security-passcode'
```

### Update Advanced Settings of course


Update the course advanced settings by adding `zoom_xblock` to the list of advanced settings.

## Usage

Publish the XBlock from Studio, and then start the Zoom meeting from the LMS.



