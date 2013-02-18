import collections

def group(data, by=[0], count=False, sum=None, avg=None, mins=None, maxs=None, returnas='detect'):
    '''group data by item and aggregate

    '''
    agg_sum = {}
    agg_avg = {}
    agg_min = {}
    agg_max = {}
    if type(by) not in (list, tuple, type(None)):
        by = [by]
    if type(sum) not in (list, tuple, type(None)):
        sum = [sum]
    if type(avg) not in (list, tuple, type(None)):
        avg = [avg]
    if type(mins) not in (list, tuple, type(None)):
        mins = [mins]
    if type(maxs) not in (list, tuple, type(None)):
        maxs = [maxs]
    if hasattr(data, '__getitem__'):
        for name, arg in [('sum',sum),('mins',mins),('avg',avg),('maxs',maxs)]:
            if arg is not None:
                for i in arg:
                    if type(i) is int and i >= len(data[0]):
                        raise ValueError(name +" is out of range")
    counter = collections.Counter()
    for item in data:
        key = tuple([item[i] for i in by])
        counter[key] += 1
        if key not in agg_sum:
            agg_sum[key] = collections.defaultdict(int)
        if avg is not None:
            if key not in agg_avg:
                agg_avg[key] = {}
            for avgi in avg:
                agg_sum[key][avgi] = agg_sum[key][avgi] + item[avgi]
                if avgi not in agg_avg[key]:
                    agg_avg[key][avgi] = item[avgi]
                else:
                    agg_avg[key][avgi] = agg_sum[key][avgi] / counter[key]
        if sum is not None:
            for sumn in set(sum).difference(avg) if avg is not None else sum:
                agg_sum[key][sumn] = agg_sum[key][sumn] + item[sumn]
        if mins is not None:
            if key not in agg_min:
                agg_min[key] = {}
            for mini in mins:
                agg_min[key][mini] = min(agg_min[key][mini], item[mini]) if mini in agg_min[key] else item[mini]
        if maxs is not None:
            if key not in agg_max:
                agg_max[key] = {}
            for maxi in maxs:
                agg_max[key][maxi] = max(agg_max[key][maxi], item[maxi]) if maxi in agg_max[key] else item[maxi]
    if returnas == 'detect':
        if (sum and type(sum[0]) is str) or (avg and type(avg[0]) is str):
            returnas = 'dict'
        elif sum is None or type(sum[0]) is int:
            returnas = 'list'
    if returnas == 'list':
        return grouped_list(agg_sum, sum, counter, count, agg_avg, avg, agg_min, mins, agg_max, maxs)
    if returnas == 'dict':
        return grouped_dict(agg_sum, by, sum, counter, count, agg_avg, avg, agg_min, mins, agg_max, maxs)
    raise ValueError('returnas must be list or dict')

def grouped_dict(agg_sum, by, sum, counter, count,
        agg_avg, avg, agg_min, mins, agg_max, maxs):
    result = []
    for key,agg in agg_sum.items():
        row = {}
        for i, byi in enumerate(by):
            row[byi] = key[i]
        for sumby,sumval in agg.items():
            row['sum('+sumby+')'] = sumval
        if key in agg_avg:
            for avgby,avgval in agg_avg[key].items():
                row['avg('+avgby+')'] = avgval
        if key in agg_min:
            for minby,minval in agg_min[key].items():
                row['min('+minby+')'] = minval
        if key in agg_max:
            for maxby,maxval in agg_max[key].items():
                row['max('+maxby+')'] = maxval
        result.append(row)
    return result

def grouped_list(agg_sum, sum, counter, count,
        agg_avg, avg, agg_min, mins, agg_max, maxs):
    result = []
    for key in agg_sum:
        row = []
        row.extend(key)
        if sum is not None:
            #row.extend(agg_sum[key].values()) #order here could be problem
            for sumn in sum:
                row.append(agg_sum[key][sumn])
        if count:
            row.append(counter[key])
        if avg:
            for avgn in avg:
                row.append(agg_avg[key][avgn])
        if mins:
            for minn in mins:
                row.append(agg_min[key][minn])
        if maxs:
            for maxn in maxs:
                row.append(agg_max[key][maxn])
        result.append(row)
    return result
