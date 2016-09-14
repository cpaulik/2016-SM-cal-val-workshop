# datasets are at a minimum reader classes and which columns are of
# interest for metric calculation
datasets = {'GLDAS': {'class': gldas_reader, 'columns': ['086_L1']},
            'SMAP': {'class': smap_reader, 'columns': ['soil_moisture']},
            'ASCAT': {'class': ascat_reader, 'columns': ['sm']}}

process = Validation(datasets, spatial_ref='SMAP', temporal_ref='ASCAT',
                     metric_calculators={(3, 2): basic_metrics.calc_metrics,
                                         (3, 3): metrics.triple_collocation},
                     scaling_ref='GLDAS', scaling='cdf_match')
