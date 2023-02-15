from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create(device = 1):
    style = 'style="font-size:22px;"'
    xml = '<xml>\n <head<>/head>\n <body>\n'
    xml += '    <p {}>Temperature: {} c</p>\n'\
         .format(style, temperature_view(device))
    xml += '    <p {}>Wind_speed: {} c</p>\n'\
         .format(style, wind_speed_view(device))
    xml += '    <p {}>Pressure: {} c</p>\n'\
         .format(style, pressure_view(device))
    
    with open('index.xml', 'w') as page:
        page.write(xml)

    return xml

def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n' 
    xml += '    <Temperature units = "f": {}</temperature>\n'\
         .format(t)
    xml += '    <Wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
         .format(w)
    xml += '    <Pressure units ="mmHg"{}</pressure>\n'\
         .format(p)
    xml +='</xml>'
    with open('new_data.xml', 'w') as page:
        page.write(xml)

    return data