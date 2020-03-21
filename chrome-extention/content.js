/*
chrome.storage.sync.get("name", function (value) {
    console.log(value["name"] == undefined);
});

    chrome.tabs.getSelected(null, function(tab) {
        request.value = tab.title + '\n';
        request.value += tab.url;
    });

*/




async function postForm() {
    var URL = 'http://192.168.1.141:5000/1';

    var tabs = await chrome.tabs.query({active: true});
    var name = await chrome.storage.sync.get("name");
  
    var form = document.createElement('form');
    var request1 = document.createElement('input');
    var request2 = document.createElement('input');
    var request3 = document.createElement('input');
    
    form.method = 'POST';
    form.action = URL;
 
    request1.type = 'hidden'; //入力フォームが表示されないように
    request1.name = 'url';
    request1.value = tabs[0].url;
    
    request2.type = 'hidden'; //入力フォームが表示されないように
    request2.name = 'title';
    request2.value = tabs[0].title;

    request3.type = 'hidden'; //入力フォームが表示されないように
    request3.name = 'name';
    request3.value = name.name;
    
    form.appendChild(request1);
    form.appendChild(request2);
    form.appendChild(request3);
    document.body.appendChild(form); 
    form.submit();
};

function postForm2() {
    var title = '',url = '',link = '';
    chrome.tabs.getSelected(null, function(tab) {
        title = tab.title;
        url = tab.url;
        link = tab.title;
    });
    var form = document.createElement('form');
    document.body.appendChild(form);
    var input = document.createElement('input');
    input.setAttribute('type','hidden');
    //input.setAttribute('title', title);
    input.setAttribute('link', link);
    form.appendChild(input);
    form.setAttribute('action', 'http://192.168.1.141:5000/1');
    form.setAttribute('method', 'POST');
    form.submit();
}

window.addEventListener("click", postForm, false);
