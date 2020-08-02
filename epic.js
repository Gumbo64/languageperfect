function getElementByXpath(path) {
    return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}
getElementByXpath('/html/head/style[7]/text()).outerHTML=""');
function deleted(id){
    document.getElementById(id).outerHTML="";
}
deleted('backgroundImage')
document.querySelector("#viewport > div.main-view-segment.gsapify-router.ng-scope > ui-view > div.v-group.game-page.notranslate.ng-scope > div.game-action-bar.classic-action-bar.v-group.ng-scope.ng-isolate-scope").outerHTML="";
document.querySelector("#question-action-bar").outerHTML='';
document.querySelector("#electronic-voice-label").outerHTML='';
document.querySelector("#content-block > div.prompt-block > div").outerHTML='';
document.querySelector("#viewport > div.main-view-segment.gsapify-router.ng-scope > ui-view > div.game-dialogs-container.ng-scope.ng-isolate-scope").outerHTML="";