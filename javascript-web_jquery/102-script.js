#!/usr/bin/node
$(document).ready(function() {
  $('#btn_translate').click(function() {
    const langCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${langCode}`, function(data) {
      $('#hello').text(data.hello);
    });
  });
});
