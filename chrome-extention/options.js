function save_options() {
  var name = document.form.name.value
  chrome.storage.sync.set({
    name:name
  }, function() {
    // 保存できたら、画面にメッセージを表示(0.75秒だけ)
    var status = document.getElementById('status');
    status.textContent = 'Options saved';
    setTimeout(function() {
      status.textContent = '';
    }, 750);
  });
}

function restore_options() {
  chrome.storage.sync.get({
    name: 'hoge',
  }, function(value) {
    document.form.name.value = value.name;
  });
}
 
// 画面表示と保存ボタンのイベントを設定
document.addEventListener('DOMContentLoaded', restore_options);
document.getElementById('save').addEventListener('click', save_options);
