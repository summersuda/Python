import pygal
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

"""
需要安装pygal_maps_world才能是要World 地图
# render_in_browser需要安装lxml
""" 

def show_east_asia():
    wm_style = RS("#336699", base_style=LCS)
    worldmap_chart = pygal.maps.world.World(style=wm_style)
    worldmap_chart.title = 'East Asia'
    worldmap_chart.add('East Asia', ['cn', 'jp', 'kr'])
    #worldmap_chart.render_in_browser()
    worldmap_chart.render_to_file('east_asia.svg')

def show_supranational_world():
    wm_style = RS("#336699", base_style=LCS)
    supra = pygal.maps.world.SupranationalWorld(style=wm_style)
    supra.add('Asia', [('asia', 1)])
    supra.add('Europe', [('europe', 1)])
    supra.add('Africa', [('africa', 1)])
    supra.add('North america', [('north_america', 1)])
    supra.add('South america', [('south_america', 1)])
    supra.add('Oceania', [('oceania', 1)])
    supra.add('Antartica', [('antartica', 1)])
    #supra.render_to_browser()
    supra.render_to_file('supranational_world.svg')

show_east_asia()
show_supranational_world()
