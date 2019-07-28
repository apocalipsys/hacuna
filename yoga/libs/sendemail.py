import smtplib
import email.message


class EnviarEmail:
    server = smtplib.SMTP('smtp.gmail.com:587')

    email_content = """
    <html>
    
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    
       <title>Gracias por Inscribirte al curso</title>
       <style type="text/css">
        a {color: #d8b20a;}
      body, #header h1, #header h2, p {margin: 0; padding: 0;}
      #main {border: 1px solid #cfcece;}
      img {display: block;}
      #top-message p, #bottom p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
      #header h1 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
      #header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
      h5 {margin: 0 0 0.8em 0;}
        h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
      p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}
       </style>
    </head>
    
    <body>
    
    
    <table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td>
    <table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
        <tr>
          <td align="center">
            <p><a href="#">Ver en Navegador</a></p>
          </td>
        </tr>
      </table>
    
    <table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
        <tr>
          <td>
            <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
              <tr>
                <td width="570" align="center"  bgcolor="#d8b60a"><h1>Hacuna Mc Yoga capo</h1></td>
              </tr>
              <tr>
                <td width="570" align="right" bgcolor="#d8b60a"><p>Julio 2019</p></td>
              </tr>
            </table>
          </td>
        </tr>
    
        <tr>
          <td>
            <table id="content-3" cellpadding="0" cellspacing="0" align="center">
              <tr>
                  <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                  <img src="https://www.popolis.it/wp-content/uploads/2019/01/sunrise-3848628_960_720-Copia.jpg" width="250" height="150"  />
                </td>
                  <td width="15"></td>
                <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                    <img src="https://image.freepik.com/foto-gratis/mujer-haciendo-pino-playa-al-atardecer_1286-32.jpg?1" width ="250" height="150" />
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td>
            <table id="content-4" cellpadding="0" cellspacing="0" align="center">
              <tr>
                <td width="200" valign="top">
                  <h5>La mejor encheniancha de choga</h5>
                  <p>En el mundo del yoga somos expertos y capos, el curso te va a enseniar a ser un master de los masters masters sayayin y ademas... CAPO!</p>
                </td>
                <td width="15"></td>
                <td width="200" valign="top">
                  <h5>Clases informativas: Venite a escuchar y ver cosas locas</h5>
                  <p>Expertos super sayayines capos y grosos mostrandote y hablandote de lo mucho que saben para que quedes como un maso </p>
                </td>
              </tr>
            </table>
          </td>
        </tr>
    
    
      </table>
      <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
        <tr>
          <td align="center">
            <p>Todos los derechos reservados a HACUNA!</p>
            <p><a href="#">Facebook</a> | <a href="#">Tweeter</a> | <a href="#">Instragram</a></p>
          </td>
        </tr>
      </table><!-- top message -->
    </td></tr></table><!-- wrapper -->
    
    </body>
    </html>
    
    
    """
    def __init__(self,email_to):
        self.email = email_to

        self.msg = email.message.Message()
        self.msg['Subject'] = 'Gracias por inscribirte al curso de Master en YOGA'

        self.msg['From'] = 'martinvargas82@gmail.com'
        self.msg['To'] = self.email
        self.password = "nirvanakurt"
        self.msg.add_header('Content-Type', 'text/html')
        self.msg.set_payload(self.email_content)

        self.s = smtplib.SMTP('smtp.gmail.com: 587')
        self.s.starttls()



    def send(self):
        # Login Credentials for sending the mail
        self.s.login(self.msg['From'], self.password)

        self.s.sendmail(self.msg['From'], [self.msg['To']], self.msg.as_string())