#!/usr/bin/env python

import ipywidgets as widgets
from ipywidgets import VBox, HBox, Text, HTML, Dropdown, Button

def CMCT_select_data_parameters():
    # CMCT Data Selection Widgets
    region_w = Dropdown(options=["greenland", "antarctica"], value='greenland', description='region:')
    mission_w = Dropdown(options=['icesat-glas', 'ers1', 'ers2', 'envisat'], value='icesat-glas', description='Mission:')
    dataset_w = Dropdown(options=["icesat-cmctnc-tpelev-grn"], value='icesat-cmctnc-tpelev-grn', description='Dataset:')
    year_w = Dropdown(options=['2003', '2004', '2005'], value='2003', description='Year:')
    var_w = Dropdown(options=["orog", "lithk", "usrf"], value='orog', description='Variable:')
    spacing_w = Dropdown(options=['1.0', '5.0', '8.0', '10.0', '16.0'], value='5.0', description='Spacing:')
    
    # User Input Widgets
    loginname_widget = Text(value='rbasnet', description='Login Name:')
    email_widget = Text(value='ritu.basnet@nasa.gov', description='Email:')
    modelname_widget = Text(value='DenisTest-2024Jan03', description='Model Name:')
    
    actualusername_label = HTML('Actual User Name:', layout={'width': '150px'})
    actualusername_input = Text(value='Ritu Basnet', layout={'width': '250px'})
    actualusername_widget = HBox([actualusername_label, actualusername_input])
    
    model_time_index_label = HTML('Model Time Index:', layout={'width': '150px'})
    model_time_index_input = Text(value='2', layout={'width': '250px'})
    model_time_index_widget = HBox([model_time_index_label, model_time_index_input])

    # Update functions for dynamic dropdowns
    def update_datasets(*args):
        region = region_w.value
        mission = mission_w.value
        if mission == 'icesat-glas':
            dataset_w.options = ["icesat-cmctnc-tpelev-grn", "icesat-cmctnc-wgselev-grn",  "icesat-cmctnc-egmmtelev-grn",
                   "icesat-cmctnc-egmtfelev-grn"] if region == 'greenland' else ["icesat-cmctnc-tpelev-ant", "icesat-cmctnc-wgselev-ant",  "icesat-cmctnc-egmmtelev-ant",
           "icesat-cmctnc-egmtfelev-ant"]
        elif mission == 'ers1':
            dataset_w.options = ["ers1-cmctnc-wgselev-grn", "ers1-cmctnc-egmmtelev-grn", "ers1-cmctnc-egmtfelev-grn"] if region == 'greenland' else ["icesat-cmctnc-tpelev-ant", "icesat-cmctnc-wgselev-ant",  "icesat-cmctnc-egmmtelev-ant"]   

    def update_years(*args):
        mission = mission_w.value
        if mission == 'icesat-glas':
            year_w.options = ['2003', '2004', '2005', '2006', '2007', '2008', '2009']
        elif mission == 'ers1':
            year_w.options = ['1991', '1992', '1993', '1994', '1995', '1996']
        # Add other missions as needed

    # Observe changes in widgets
    region_w.observe(update_datasets, 'value')
    mission_w.observe(update_datasets, 'value')
    mission_w.observe(update_years, 'value')

    # Collect all widgets in a vertical layout
    all_widgets = VBox([region_w, mission_w, dataset_w, year_w, var_w, spacing_w, 
                        loginname_widget, email_widget, modelname_widget, 
                        actualusername_widget, model_time_index_widget])

    # Display all widgets
    display(all_widgets)
    
    # Return a dictionary of the current values
    return {
        'region': region_w.value,
        'mission': mission_w.value,
        'dataset': dataset_w.value,
        'year': year_w.value,
        'variable': var_w.value,
        'spacing': spacing_w.value,       
        'loginname_widget': loginname_widget.value,
        'email': email_widget.value,
        'model_name': modelname_widget.value,
        'actual_user_name': actualusername_input.value,
        'model_time_index': model_time_index_input.value
    }







