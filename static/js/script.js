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
        // var words_data = $.parseJSON(data);
        console.log(data)
        
        // data = [4, 15, 7];
        labels =  ["positif", "netral", "negatif"];
        renderChart(data, labels);
    }});

   
});

function renderChart(data, labels) {
    var ctx = document.getElementById("myBarChart").getContext('2d');
    var mixChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                // {
                //     type: 'line',
                //     label: "Revenues",
                //     data: data,
                //     borderColor: 'rgba(75, 192, 192, 1)',
                //     backgroundColor: 'rgba(0, 0, 0, 0)',
                //     yAxisID: 'revenues',
                // },
                {
                    label: "Clients",
                    data: data,
                    borderColor: 'rgba(0, 0, 0, 0)',
                    backgroundColor: 'rgba(192, 75, 192, 0.5)',
                    yAxisID: 'clients',
                }
            ]
        },
        options: {
            scales: {
                yAxes: [
                    {
                        id: "revenues",
                        ticks: {
                            beginAtZero: true,
                        },
                        scaleLabel: {
                            display: true,
                            labelString: 'Revenues (U$)'
                          }
                    },
                    {
                        id: "clients",
                        position: 'right',
                        ticks: {
                            beginAtZero: true,
                        },
                        scaleLabel: {
                            display: true,
                            labelString: 'Clients'
                          }
                    },
                ]
            },
        }
    });
}
