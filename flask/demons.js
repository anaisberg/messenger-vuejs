// wonderful jquery-based demons client application
$(document).ready(function () {

  // change channel by updating the demons iframe src
  $('#select-channel').click(function () {
    $('#demons').attr('src', '/' + $('#channel-name').val() + '/pull');
  });

  // rough posting on current channel
  $('#send-message').click(function () {
    $.get('/' + $('#channel-name').val() +
          '/post/' + $('#message').val(), null, 'text');
  });

  // reload demons iframe every 3 seconds by re-assigning src
  setInterval(function () {
    $('#demons').attr('src', $('#demons').attr('src'));
  }, 3000);
});
