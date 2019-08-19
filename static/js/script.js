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

   $.ajax({url: '/sentiment', success: function (data) {
    // returned data is in string format we have to convert it back into json format
    var sentiment_data = $.parseJSON(data);

    var ctx = document.getElementById("myBarChart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'This week',
                data: sentiment_data,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
            }]
        },
        options: {            
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        callback: function(value, index, values) {
                            return float2dollar(value);
                        }
                    }
                }]                
            }
        },
    });
}});
});
