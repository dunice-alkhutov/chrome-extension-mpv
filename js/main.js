/**
 * A simple example.
 * Register a click on links, if URI mathes REGEXP, send message to native video player
 */

const REGEXP = {
  youtube: /http(s)?:\/\/(www.)?youtube.com\/watch\?v=.+/i,
  twitch: /http(s)?:\/\/(www.)?twitch.tv\/[\w]+/i
};
Object.freeze(REGEXP);

function sendToNativeApp(data) {
  return new Promise((resolve, reject) => {
    chrome.runtime.sendNativeMessage('com.mpv.app', data,
      function(response) {
        return resolve(response)
      });
  })
}

async function startPlay(url) {
  for (var key in REGEXP) {
    if (url.match(REGEXP[key])) {
      return await sendToNativeApp({ url, type: key });
    }
  }
  return null;
}

// A generic onclick callback function.
function genericOnClick(info, tab) {
  startPlay(info.linkUrl).then(resp => {
    if(resp.code !== 1) {
      console.error(`Can't play a video: ${resp.code}`);
    }
  })
}

chrome.contextMenus.onClicked.addListener(genericOnClick);

// Set up context menu at install time.
chrome.runtime.onInstalled.addListener(function() {
  const menuItem = {
    id: 'mpvMenu',
    title: 'Start with MPV',
    contexts: ['link']
  };
  chrome.contextMenus.create(menuItem);
});