$(document).ready(function () {
    // on page load this will fetch data from our flask-app asynchronously
   $.ajax({url: '/word_cloud', success: function (data) {
       // returned data is in string format we have to convert it back into json format
       var words_data = $.parseJSON(data);
       // we will build a word cloud into our div with id=word_cloud
       // we have to specify width and height of the word
       $('#word_cloud').jQCloud(words_data, {
           width: 600,
           height: 300
       });
   }});
});
