import bar_chart_race as bcr
import pandas as pd
import time

tic = time.perf_counter()

df = pd.read_csv("https://raw.githubusercontent.com/onithish/Bar_Chart_Race_AAUM/main/data.csv", index_col=0)
# df.fillna(0.00, inplace=True)
# df.to_csv("C:\python\Working\Automate-Learnings\bar_chart_race\data.csv")

# using the bar_chart_race package
bcr.bar_chart_race(
    # must be a DataFrame where each row represents a single period of time.
    df=df,
    # number of bars to display in each frame
    n_bars=12,
    # smoothness of the animation
    steps_per_period=25,
    # time period in ms for each row
    period_length=350,
    title='  ',
    filter_column_colors=True,
    period_label={'x': .98, 'y': .3, 'ha': 'right', 'va': 'center'},
    period_summary_func=lambda v, r: {'x': .98, 'y': .2, 
                                        's': f'Industry AUM: Rs. {v.sum():,.0f} Cr', 
                                        'ha': 'right', 'size': 11},
    bar_size=.95, 
    scale='linear', 
    fig=None, 
    writer=None, 
    bar_kwargs={'alpha': .7},
    shared_fontdict={'family': 'cursive', 'weight': 'semibold', 'color': 'darkslategrey'},
    cmap = 'tab20',
    # name of the video file
    filename="C:\\python\\Working\\Automate-Learnings\\bar_chart_race\\video4.mp4"
    )

toc = time.perf_counter()
print(f"Downloaded the data in {(toc - tic)/60:0.0f} minutes {(toc - tic)%60:0.0f} seconds")
