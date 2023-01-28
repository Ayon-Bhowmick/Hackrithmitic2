import matplotlib.pyplot as plt
import io
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
    def labelBars(rects, xpos):
        ha = {"right": "left", "left": "right"}
        offset = {"right": 1, "left": -1}

        for rect in rects:
            height = rect.get_height()
            ax.annotate("{}".format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),
                    textcoords="offset points",
                    ha=ha[xpos], va="bottom")

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
    labelBars(rects1, "left")
    labelBars(rects2, "right")
    fig.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return "data:image/png;base64,{}".format(urllib.parse.quote(image_base64))

graphAirlines(test_airlines)
