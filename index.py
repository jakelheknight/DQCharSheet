#!/usr/bin/python3
import cgitb
import pymysql

print("Content-type: text/html\n\n")
dataBase = pymysql.connect(host='localhost', user='root', passwd='J3w31kni', db='CharSheet')

c = dataBase.cursor()
sql = "SELECT * FROM basicStats WHERE id=2"

c.execute(sql)
results = c.fetchall()
for row in results:
	PS = row[1]
	MD = row[2]
	AG = row[3]
	MA = row[4]
	WP = row[5]
	EN = row[6]
	Name = row[7]
	PB = row[8]
	Race = row[9]
	Aspect = row[10]
	Status = row[11]
	Birth = row[12]
	Hand = row[13]
	
dataBase.close()

print("""
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>DQ Charicter Sheet</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">
  <script>""")
print("var PS =",PS)
print("var MD =",MD)
print("var AG =",AG)
print("var MA =",MA)
print("var WP =",WP)
print("var EN =",EN)
print('var Name = "'+Name+'"')
print("var PB =",PB)
print('var Race = "',Race+'"')
print('var Aspect= "',Aspect+'"')
print('var Social = "',Status+'"')
print('var Birth = "',Birth+'"')
print('var Hand = "',Hand+'"')
print("""</script>
  <script src="JavaScript/charSht.js">
  </script>
  <link rel="stylesheet" type="text/css" href="CSS/charSheet.css">

  <!--[if lt IE 9]>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>
  <![endif]-->
</head>
<body onload="updateFN()">
    <div id="Pic">
    <!--This is the base states table-->   
    </div>
    <div class="stats">
        <table class="baseST">
            <thead>
                <tr>
                    <th id="DQtitle" colspan="5" rowspan="2">Dragon Quest</th><th colspan="6">Priamry Charicteristics <button onclick="updateFN()"> Update </button></th>
                </tr> 
                <tr>
                    <th>
                        <table>
                            <tr>
                                <td>PS</td><td id="PStot"></td>
                            </tr>
                            <tr>
                                <td></td><td id="PS"></td>
                            </tr>
                        </table>
                    </th>
                    <th><table>
                            <tr>
                                <td>MD</td><td id="MDtot"></td>
                            </tr>
                            <tr>
                                <td></td><td id="MD">13</td>
                            </tr>
                        </table>                        
                    </th>
                    <th><table>
                            <tr>
                                <td>AG</td><td id="AGtot"></td>
                            </tr>
                            <tr>
                                <td></td><td id="AG">13</td>
                            </tr>
                        </table>
                    </th>
                    <th><table>
                            <tr>
                                <td>MA</td><td id="MAtot"></td>
                            </tr>
                            <tr>
                                <td></td><td id="MA">13</td>
                            </tr>
                        </table>
                    </th>
                    <th><table>
                            <tr>
                                <td>WP</td><td id="WPtot"></td>
                            </tr>
                            <tr>
                                <td></td><td id="WP">13</td>
                            </tr>
                        </table>                        
                    </th>
                    <th><table>
                            <tr>
                                <td>EN</td><td id="ENtot"></td>
                            </tr>
                            <tr>
                                <td><button onclick="damageEN()">EN Dmg</button></td><td id="EN">13</td>
                            </tr>
                        </table>
                    </th>
                </tr>
                </thead>
            <tfoot>
            </tfoot>
            <tbody>
                <tr>
                    <th colspan="6">
                        <table>
                            <tr>
                                <td>Charicter Name:</td><td id="charName">Jax</td>
                            </tr>
                        </table>
                    
                    </th>
                    <th>
                        <table>
                            <tr>
                                <td>PC</td><td id="PC">8</td>
                            </tr>
                        </table>
                    
                    </th>
                    <th>
                        <table>
                            <tr>
                                <td>TMR</td><td id="TMR">8</td>
                            </tr>
                        </table>
                    
                    </th>
                    <th>
                        <table>
                            <tr>
                                <td>PB</td><td id="PB">8</td>
                            </tr>
                        </table>
                    
                    </th>
                    <th rowspan="2">
                        <table>
                            <tr>
                                <td>DEF</td><td id="DEF"></td>
                            </tr>
                            <tr>
                                <td></td><td id="DEFtot">8</td>
                            </tr>
                        </table>                  
                    </th>
                    <th rowspan="2">
                        <table>
                            <tr>
                                <td>FT</td><td id="FTtot"></td>
                            </tr>
                            <tr>
                                <td><button onclick="damage()">Dmg</button></td><td id="FT"></td>
                            </tr>
                        </table>                    
                    </th>
                </tr>
                <tr>
                    <th colspan="2">
                        <table>
                            <tr>
                                <td>Race</td><td id="Race">human</td>
                            </tr>
                        </table>
                    </th>
                    <th colspan="2">
                        <table>
                            <tr>
                                <td>Aspect</td><td id="Aspect">8</td>
                            </tr>
                        </table>
                    </th>
                    <th colspan="2">
                        <table>
                            <tr>
                                <td >Social Status</td><td id="Social">8</td>
                            </tr>
                        </table>
                    </th>
                    <th colspan="2">
                        <table>
                            <tr>
                                <td>Birth</td><td id="Birth">8</td>
                            </tr>
                        </table>
                    </th>
                    <th>
                        <table>
                            <td>Hand</td><td id="Hand"> A</td>
                        </table>
                    </th>
                </tr>            
            </tbody>
        </table>
        
    </div>
</body>
</html>""")
