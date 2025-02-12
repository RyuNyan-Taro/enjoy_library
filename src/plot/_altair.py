import altair as alt
from vega_datasets import data
from typing import Optional


def plot_sample_data(dataset_name: str, x: Optional[str] = None, y: Optional[str] = None):

    _data = getattr(data, dataset_name)()

    if x and y:

        # make the chart
        alt.Chart(_data).mark_point().encode(
            x=x,
            y=y,
            color='Origin',
        ).interactive()

    else:
        print(_data.info())


def show_dataset_names():
    print([d for d in dir(data) if not d.startswith("_")])
