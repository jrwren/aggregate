# module aggregate:

## NAME
    aggregate - a helper of list of lists and list of dicts

## FILE
    aggregate.py

## INSTALLATION
    pip install git+https://github.com/jrwren/aggregate.git

## DESCRIPTION

    Module enabling aggregation of data in simple list of list or list of dicts.

    As an example, here is the result of calling the group function on this data:

        data = [ ( 'Lilly', '2013-2-16', 50 ),
                 ( 'Lilly', '2013-2-15', 20 ),
                 ( 'Dad', '2013-2-16', 10 ),
                 ( 'Dad', '2013-2-15', 10 ),
                 ( 'Mom', '2013-2-16', 10 ) ]
        #group data by index 0 and sum index 2
        aggregate.group(data, by=0, sum=2)
        [['Dad', 20], ['Lilly', 70], ['Mom', 10]]

    List of dicts use names for group by and aggregate args and return lists of
    dicts with aggregate names as key values (similar to sql).

         data = [ { 'name':'Lilly', 'date':'2013-2-16', 'score':50},
                  { 'name':'Lilly', 'date':'2013-2-15', 'score':20},
                  { 'name':'Dad', 'date':'2013-2-15', 'score':10},
                  { 'name':'Dad', 'date':'2013-2-16', 'score':10},
                  { 'name':'Mom', 'date':'2013-2-16', 'score':10}]
         aggregate.group(data, by='name', sum='score')
        [{'sum(score)': 20, 'name': 'Dad'},
         {'sum(score)': 70, 'name': 'Lilly'},
         {'sum(score)': 10, 'name': 'Mom'}]

    * note: this example data is for a game where lowest score is better. Mom 0wnz.

## LICENSE
Apache 2 License

## VERSION
0.0.1

## DATE
2/17/2013

## AUTHOR
Jay R. Wren
