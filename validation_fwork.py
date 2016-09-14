# datasets are at a minimum reader classes and which columns are of
# interest for metric calculation
datasets = {'GLDAS': {'class': gldas_reader, 'columns': ['086_L1']},
            'SMAP': {'class': smap_reader, 'columns': ['soil_moisture']},
            'ASCAT': {'class': ascat_reader, 'columns': ['sm']}}

process = Validation(datasets, 'SMAP', {(3, 2): basic_metrics.calc_metrics,
                                        (3, 3): metrics.triple_collocation},
                     temporal_ref='ASCAT', scaling='cdf_match',
                     scaling_ref='GLDAS')
