var myChart = echarts.init(document.getElementById('main'))

function readSingleFile(e) {
    var file = e.target.files[0]
    if (!file) {
        return
    }
    var reader = new FileReader()
    reader.onload = function(e) {
        var contents = e.target.result
        displayContents(contents)
    }
    reader.readAsText(file)
}

function GetRandomColor(){
    r = Math.floor(Math.random() * 255)
    g = Math.floor(Math.random() * 255)
    b = Math.floor(Math.random() * 255)
    a = 0.6
    str = 'rgba(' + r.toString() + ',' + g.toString() + ',' + b.toString() + ',' + a.toString() + ')'
    return str
}

function displayContents(contents) {
    //myChart.setOption({},true)
    set = contents.split('\n')
    var tData = []
    var xCat = []
    var data = []
    var seriesData = []
    for (i = 0; i < set.length; i++) {
        t = set[i].split(' ')
        xCat.push(t[0])
        tData.push(t[1])
    }
    console.log(tData)
    seriesData.push(tData)

    for (i = 0; i < seriesData.length; i++) {
        str = GetRandomColor()
        data.push({
            name: 'Trip Count',
            type: 'line',
            showSymbol: true,
            hoverAnimation: false,
            itemStyle: {
                normal: {
                    color: str
                }
            },
            data: seriesData[i]
        })
    }

    option = {
        title: {
            text: '时间坐标轴'
        },
        xAxis: {
            type: 'category',
            data: xCat
        },
        yAxis: {
            type: 'value'
        },
        tooltip: {
            trigger: 'axis'
        },
        dataZoom: [
        {
            show: true,
            realtime: true,
            start: 0,
            end: 100
        },
        {
            type: 'inside',
            realtime: true,
            start: 0,
            end: 100
        }
        ],
        series: data
    }
    myChart.setOption(option)
}

document.getElementById('file-input').addEventListener('change', readSingleFile, false);