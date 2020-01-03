a = open("puspanjali.html", "w")
b = """<!doctype html>
<html>
 <head>
<title>RESUME</title>
<style type="text/css">
    table {
        font-size: 18px;
    }
    #heading{
        font-size: 20px;
        }
</style>
</head>
<center><h1><u><b> RESUME</u></b></h1></center></div>
<body style="padding-top:10px ; padding-left: 40px; padding-right:40px; " >
    <div class="col-xs-6" >

<div  >
	<div class="jumbotron">

<h3 style="font-size: 28px;">Pushpanjali Baghele</h3>
<p  style="font-size: 25px;">DOB: 06-July-2001</p>
<p  style="font-size: 25px;">Adress : Indira Gandhi Girls Hostel Bhopal </p>
<p  style="font-size: 25px;">Contact No.: 7389030668</p>
<p  style="font-size: 25px;">Nationality : Indian</p>


  <h3><u><b>CAREER OBJECTIVE</u></b></h3>
  <p  style="font-size: 25px;">To solve problems in effective and creative in a challanging  position. </p>
            <h3><u>EDUCATION </u></h3>
            <table border="" >
                <tr >
                    <th>Qualification</th>
                    <th>Institute</th>
                    <th>Percentage / Grades</th>
                    <th>Year</th>
                </tr>
                <tr>
                    <td>10th</td>
                    <td>Excellence School Balaghat</td>
                    <td>90.05%</td>
                    <td>2016</td>
                </tr>
                <tr>
                    <td>12th</td>
                    <td>Excellence School Balaghat </td>
                    <td>95.20%</td>
                    <td>2018</td>
                </tr>
                <tr>
                    <td>1st year</td>
                    <td>Barkatullah University Institute<br> Of Technology Bhopal</td>
                    <td>83.1</td>
                    <td>2019</td>
                </tr>

            </table>

        </div>
          <h3 style="text-transform: uppercase;"><u>Key Skills</u></h3>
     <ol  style="font-size: 25px;">
      <li> C++</h3>
	 <li> C</li>
	 <li> HTML</li>
	 <li> CSS</li>
	</ol>
         <h3><u>HOBBIES</u></h3>
        <ol style="font-size: 25px;"><li>Reading Story</li>
        <li>Singing</li>
        </ol>
    <h3><u style="text-transform: uppercase;">Langauges</u></h3>
    <ol style="font-size: 25px;">
        <li> English</li>
        <li>Hindi</li>
    </ol>
        <h3><u>WORK  EXPERIENCE</u></h3>
        <p style="font-size: 25px;">Fresher</p>
</div></body>
</html>"""
a.write(b)
a.close()