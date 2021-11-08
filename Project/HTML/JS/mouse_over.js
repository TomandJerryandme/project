// 酷炫鼠标轨迹动画效果js代码
window.onload = function () {
    C = Math.cos;
    S = Math.sin;
    U = 0;
    w = window;
    j = document;
    d = j.getElementById("canvas");                                                 // 返回界面中的画布元素
    c = d.getContext("2d");                                                         // getContext() 方法返回一个用于在画布上绘图的环境  canvas方法
    W = d.width = w.innerWidth;                                                     // 声明了窗口的文档显示区的高度和宽度，以像素计     即： 浏览器窗口文档(显示区域，不包含状态栏等)的高度与宽度，   outerheight： 整个浏览器大小的属性
    H = d.height = w.innerHeight;
    c.fillRect(0, 0, W, H);                                                         // fillRect() 方法绘制“已填色”的矩形 默认的填充颜色是黑色  fillRect(x, y, width, height)    x,y: 用于确定图形左上角坐标，另外两个用于确定图形的大小
    c.globalCompositeOperation = "lighter";
    /**?
     * 画布的 globalCompositeOperation 属性： 设置或返回如何将一个源（新的）图像绘制到目标（已有）的图像上
     * 属性有：
     *  source-over :   源图像在上
     *  source-atop :   源图像在上，且源图像不在目标图像的部分隐藏(且目标图像不与源图像重合的部分隐藏)
     *  source-in   :   在目标图像中显示源图像。只有目标图像内的源图像部分会显示，目标图像是透明的
     *  source-out  :   在目标图像之外显示源图像。只会显示目标图像之外源图像部分，目标图像是透明的
     *  destination-over:   目标图像在上
     *  destination-atop:   
     *  destination-in: 与上述类似在源图像中显示目标图像。只有源图像内的目标图像部分会被显示，源图像是透明的
     *  destination-out:    
     *  lighter :   显示源图像 + 目标图像   (重合部分色相变更)
     *  copy    :   显示源图像。忽略目标图像
     *  xor :   使用异或操作对源图像与目标图像进行组合(取两个图像的不重合部分)
     *  https://www.w3school.com.cn/tags/html_ref_canvas.asp        canvas手册
     */
    c.lineWidth = 0.1;                                                              // 设置或返回当前线条的宽度，以像素计   canvas属性
    c.lineCap = "round";                                                            // 设置或返回线条末端线帽的样式     canvas属性
    var bool = 0, t = 0;
    j.onmousemove = function (e) {
        if (window.T) {
            if (D == 9) {
                D = Math.random() * 15; f(1);
            } clearTimeout(T);
        }
        X = e.pageX;
        Y = e.pageY;
        a = 0;
        b = 0;
        A = X, B = Y;
        R = (e.pageX / W * 999 >> 0) / 999;
        r = (e.pageY / H * 999 >> 0) / 999;
        U = e.pageX / H * 360 >> 0; D = 9;
        g = 360 * Math.PI / 180;
        T = setInterval(f = function (e) {
            c.save();
            c.globalCompositeOperation = "source-over";
            if (e != 1) {
                c.fillStyle = "rgba(0,0,0,0.02)";
                c.fillRect(0, 0, W, H);
            }
            c.restore();
            i = 25;
            while (i--) {
                c.beginPath();
                if (D > 450 || bool) {
                    if (!bool) {
                        bool = 1;
                    }
                    if (D < 0.1) {
                        bool = 0;
                    }
                    t -= g;
                    D -= 0.1;
                }
                if (!bool) {
                    t += g;
                    D += 0.1;
                }
                q = (R / r - 1) * t;
                x = (R - r) * C(t) + D * C(q) + (A + (X - A) * (i / 25)) + (r - R);
                y = (R - r) * S(t) - D * S(q) + (B + (Y - B) * (i / 25));
                if (a) {
                    c.moveTo(a, b);
                    c.lineTo(x, y)
                }
                c.strokeStyle = "hsla(" + (U % 360) + ",100%,50%,0.75)";
                c.stroke(); a = x; b = y;
            } U -= 0.5; A = X; B = Y;
        }, 16);
    };
    j.onkeydown = function (e) { a = b = 0; R += 0.05 };
    j.onmousemove({ pageX: 300, pageY: 290 })
};