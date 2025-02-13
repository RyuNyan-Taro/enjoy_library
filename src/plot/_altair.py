import altair as alt
from vega_datasets import data
from typing import Optional


def chart_sample_data(dataset_name: str, x: Optional[str] = None, y: Optional[str] = None) -> alt.vegalite.v5.api.Chart:

    _data = getattr(data, dataset_name)()

    if x and y:

        # make the chart
        plot_class = alt.Chart(_data).mark_point().encode(
            x=alt.X(x),
            y=alt.Y(y),
            color='Origin',
        ).interactive()

        return plot_class

    else:
        print(_data.info())


def show_dataset_names():
    print([d for d in dir(data) if not d.startswith("_")])
