__all__ = ['chart_sample_data', 'show_dataset_names', 'horizontally_concat_charts', 'vertically_concat_charts']

import altair as alt
from vega_datasets import data
from typing import Optional


def chart_sample_data(dataset_name: str, x: Optional[str] = None, y: Optional[str] = None, tool_tip: Optional[list[str]] = None) -> alt.vegalite.v5.api.Chart:
    """Return a Chart plot or show information of the dataset_name.

    Args:
        dataset_name: Vega dataset name.
        x: X column name and type of altair format.
        y: Y column name and type of altair format.
        tool_tip: Tool tip for plot.

    Returns:
        The interactive altair Chart.
    """

    _data = getattr(data, dataset_name)()

    if x or y:
        _encord_items = {'color': 'Origin'}
        if x:
            _encord_items['x'] = alt.X(x)
        if y:
            _encord_items['y'] = alt.Y(y)
        if tool_tip:
            _encord_items['tool_tip'] = tool_tip

        # make the chart
        plot_class = alt.Chart(_data).mark_point().encode(**_encord_items).interactive()

        return plot_class

    else:
        print(_data.info())


def show_dataset_names():
    print([d for d in dir(data) if not d.startswith("_")])


def horizontally_concat_charts(charts: list):
    concat_chart = charts[0]

    for _chart in charts[1:]:
        concat_chart = concat_chart | _chart

    return concat_chart


def vertically_concat_charts(charts: list):
    concat_chart = charts[0]

    for _chart in charts[1:]:
        concat_chart = concat_chart & _chart

    return concat_chart


