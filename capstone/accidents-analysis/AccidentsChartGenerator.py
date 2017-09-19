import sqlite3

conn = sqlite3.connect('accidentsdb.sqlite')
cur = conn.cursor()

print("Creating output for Google Bubble chart")

# where State in ('Tamil Nadu', 'Madhya Pradesh', 'Maharashtra', 'Karnataka', 'Kerala',
# 'Andhra Pradesh', 'Uttar Pradesh', 'Gujarat', 'Rajasthan', 'Chhattisgarh')
cur.execute('''Select State, Year, Accidents, Education
from AccidentsData
where State in ('Tamil Nadu', 'Madhya Pradesh', 'Maharashtra')
Order by State, Year, Education''')

edudict = {'9to10': 9.5, 'Upto8': 8, 'Above10': 12}
fhand = open('bubblechart.html', 'w')
fhand.write('''<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawSeriesChart);

    function drawSeriesChart() {
      	var data = google.visualization.arrayToDataTable([
		['ID', 'Year', 'Accidents', 'State', 'Education'],\n''')

for row in cur:
    state = row[0]
    year = str(row[1])
    accidents = str(row[2])
    edu = str(edudict.get(row[3]))
    #print(state, year, accidents, edu)
    fhand.write("\t\t['', " + year + ", " + accidents + ", '" + state + "', " + edu + "],\n")

fhand.write('\t\t]);\n')
fhand.write('''\nvar options = {
          title: 'Road Accidents in India classified according to Education level of Drivers',
          hAxis: {
            title: 'Year'
          },
          vAxis: {
            title: 'Number of Accidents'
          },
          bubble: {
            textStyle: {
              fontSize: 11
            }
          }
        };

      var chart = new google.visualization.BubbleChart(document.getElementById('series_chart_div'));
      chart.draw(data, options);
    }
    </script>
  </head>
  <body>
    <div id="series_chart_div" style="width: 1500px; height: 800px;"></div>
  </body>
</html>''')
fhand.close()
cur.close()

print("Done writing bubblechart.html")
