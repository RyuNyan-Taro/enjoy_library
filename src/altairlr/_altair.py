__all__ = [
    'chart_sample_data', 'chart_selected_mark', 'chart_with_encode_items', 'chart_with_layout',
    'show_dataset_names', 'show_mark_types',
    'get_mark_types', 'horizontally_concat_charts', 'vertically_concat_charts']

import altair as alt
from vega_datasets import data
from typing import Optional, Union


def chart_sample_data(dataset_name: str, x: Optional[str] = None, y: Optional[str] = None,
                      tool_tip: Optional[list[str]] = None) -> alt.vegalite.v5.api.Chart:
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


def chart_selected_mark(dataset_name, x: str, y: str, mark_type: str) -> alt.vegalite.v5.api.Chart:
    _data = getattr(data, dataset_name)()
    _chart = alt.Chart(_data)
    _mark = getattr(_chart, 'mark_' + mark_type)

    return _mark().encode(alt.X(x), alt.Y(y))


def chart_with_encode_items(dataset_name: str, x: str, y: str, encode_items: list) -> alt.vegalite.v5.api.Chart:
    _data = getattr(data, dataset_name)()

    return alt.Chart(_data).mark_point().encode(alt.X(x), alt.Y(y), *encode_items)


def chart_with_layout(dataset: Union[alt.ChartDataType, str], x: str, y: str,
                      mark_layout: Optional[dict], x_layout: dict, y_layout: dict,
                      encode_items: Optional[list] = None) -> alt.vegalite.v5.api.Chart:
    if isinstance(dataset, str):
        dataset = getattr(data, dataset)()

    if mark_layout:
        _chart = alt.Chart(dataset).mark_point(**mark_layout)
    else:
        _chart = alt.Chart(dataset).mark_point()

    if encode_items:
        return _chart.encode(
            alt.X(x, **x_layout),
            alt.Y(y, **y_layout),
            *encode_items
        )

    return _chart.encode(
            alt.X(x, **x_layout),
            alt.Y(y, **y_layout)
        )


def show_dataset_names():
    print([d for d in dir(data) if not d.startswith("_")])


def show_mark_types():
    print(_mark_types_list())


def get_mark_types():
    return _mark_types_list()


def _mark_types_list() -> list[str]:
    return [method.split('_')[1] for method in dir(alt.Chart) if method.startswith("mark_")]


def horizontally_concat_charts(charts: list) -> list:
    concat_chart = charts[0]

    for _chart in charts[1:]:
        concat_chart = concat_chart | _chart

    return concat_chart


def vertically_concat_charts(charts: list) -> list:
    concat_chart = charts[0]

    for _chart in charts[1:]:
        concat_chart = concat_chart & _chart

    return concat_chart
