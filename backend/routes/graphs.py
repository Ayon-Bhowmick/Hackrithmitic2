import matplotlib.pyplot as plt
from io import BytesIO
import urllib, base64
import numpy as np

test_airlines = {
    "delta": {
        "pos": 3,
        "neg": 2
    },
    "american": {
        "pos": 4,
        "neg": 6
    }
}



def graphAirlines(data = test_airlines):
    def labelBars(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate("{}".format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha="center", va="bottom")

    pos = [data[x]["pos"] for x in data.keys()]
    neg = [data[x]["neg"] for x in data.keys()]
    names = [x for x in data.keys()]
    ind = np.arange(len(pos))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, pos, width, label="Positive")
    rects2 = ax.bar(ind + width/2, neg, width, label="Negative")
    ax.set_ylabel("Number of Reviews")
    ax.set_title("Airline Sentiment")
    ax.set_xticks(ind)
    ax.set_xticklabels(names)
    ax.legend()
    labelBars(rects1)
    labelBars(rects2)
    fig.tight_layout()
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf
    # buf = io.BytesIO()
    # plt.savefig(buf, format='png')
    # buf.seek(0)
    # image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    # # return "data:image/png;base64,{}".format(urllib.parse.quote("image_base64"))
    # return "data:image/png;base64,{}".format(urllib.parse.quote("ayon.png"))

graphAirlines(test_airlines)
