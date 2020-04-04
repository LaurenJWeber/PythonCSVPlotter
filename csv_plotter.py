#!/usr/bin/python3

###############################################################################
# Description:  Plot a rectangular block of CSV data using Matplotlib.
#               Plot all y columns against a common x-axis.
# Usage:        Supply the name of a csv file as a command-line argument.
#               Optionally, specify the type of plot: line, or scatter.
#               Optionally, specify a title for the plot.
#               Optionally, specify the placement of the legend.
#               Rows beginning with "#" or "//" are ignored as comments.
# Important:    All rows must have the same number of data points, i.e.
#               the data set must be rectangular, not jagged.
#               The first complete non-comment row in the CSV file will be
#               used as the column headings.
################################################################################

import matplotlib.pyplot as plotter
import argparse
import sys
from exitstatus import ExitStatus


def is_comment(csv_line):
    return csv_line.startswith("//") or csv_line.startswith("#")


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", help="Path to csv data file.")
    parser.add_argument("plot_type", help="Plot type: scatter or line", default="line", nargs="?")
    parser.add_argument("plot_title", help="Title of plot", default="", nargs="?")
    parser.add_argument("legend_placement", help="Placement of legend", default="best", nargs="?",
                        choices={"upper left", "center left", "lower left", "best",
                                 "upper right", "center right", "lower right", "right",
                                 "upper center", "lower center", "center"
                                 })
    args = parser.parse_args()

    x_values = []
    x_values_heading = ""
    y_values_headings = []
    y_values_columns = []
    line_count = 1
    one_by_one_grid_first_subplot = 111

    with open(args.data_path, "r") as csv_data:
        for line in csv_data:

            line = line.strip()

            if is_comment(line):
                line_count += 1
                continue

            row = line.split(",")

            if x_values_heading == "":
                x_values_heading = row[0]
                y_values_headings = row[1:]
                num_y_columns = len(y_values_headings)
                for i in range(num_y_columns):
                    y_values_columns.append([])
            else:
                if len(row) - 1 != num_y_columns:
                    print("Line", line_count, ": expected", num_y_columns + 1, "columns, found",
                          len(row), "- skipping row.")
                else:
                    try:
                        x_values.append(float(row[0]))
                        for i in range(num_y_columns):
                            y_values_columns[i].append(float(row[i+1]))

                    except ValueError as val_error:
                        print("Line ", line_count, "of CSV file is incorrectly formatted.  "
                              "\nEnsure data set is rectangular,",
                              "and y-values columns contain numeric values.",
                              "\nException message:", str(val_error))
                        sys.exit(ExitStatus.failure)

            line_count += 1

    fig = plotter.figure()
    ax1 = fig.add_subplot(one_by_one_grid_first_subplot)

    for i in range(0, len(y_values_headings)):
        if args.plot_type.lower() == "line":
            ax1.plot(x_values, y_values_columns[i], marker='.', label=y_values_headings[i])
        else:
            ax1.scatter(x_values, y_values_columns[i], marker='.', s=2, label=y_values_headings[i])

    if args.plot_title != "":
        ax1.set_title(args.plot_title)

    plotter.xlabel(x_values_heading)
    plotter.legend(loc=args.legend_placement)
    plotter.show()


if __name__ == "__main__":
    main()
