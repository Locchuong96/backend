from flask import Flask 
import folium

app = Flask(__name__)

@app.route("/")
def base():
    #this is basemap
    my_map = folium.Map(location = [43.52336,-122.6750])
    return my_map._repr_html_()

@app.route("/open-street-map")
def open_street_map():
    my_map = folium.Map(loation = [43.52336,-122.6750],tiles = "Stamen Toner")
    return my_map._repr_html_()

@app.route("/map-marker")
def map_marker():
    my_map = folium.Map(location = [45.52336,-122.6750],tiles='Stamen Terrain',zoom_start =12)

    folium.Marker(location = [45.52336,-122.6750],
                    popup = "<b>Marker<b>",
                    tooltip = "Click here!").add_to(my_map)
    
    return my_map._repr_html_()

if __name__ == "__main__":
    app.run(debug = True)