# PythonCSVPlotter

Read a CSV file containing a rectangular block of data, use Python and Matplotlib to plot the data.

Plot all y columns against a common x-axis.


## Usage      
  
Supply the name of a csv file as a command-line argument.

Optionally, specify the type of plot: line, or scatter.

Optionally, specify a title for the plot.

Optionally, specify the placement of the legend.

Rows beginning with "#" or "//" are ignored as comments.

## Examples

`python3 csv_plotter.py awards_viewers.csv line "Awards Viewership vs. Year" "center left"`

`python3 csv_plotter.py algebraic_functions.csv line "Algebraic Functions" best`

## Important    

All rows must have the same number of data points, i.e.

the data set must be rectangular, not jagged.

The first complete non-comment row in the CSV file will be used as the column headings.