function fly(event) {
  if ($("#u-flyer-img").length) {
    return
  }
  var offset = $(".fly_end").offset();
  var fly = $(".app");
  var img = $('.goods_detail_pic').find('img').attr('src');
  var flyer = $('<img id="u-flyer-img" class="u-flyer" src="'+img+'">');
  var hei=$(window).scrollTop();
  fly.css("cursor","wait").unbind('click');

  flyer.fly({
    start: {
      left: event.pageX, //开始位置（必填）#fly元素会被设置成position: fixed
      top: event.pageY - hei //开始位置（必填）
    },
    end: {
      left: offset.left+10, //结束位置（必填）
      top: offset.top+10, //结束位置（必填）
      width: 0, //结束时宽度
      height: 0 //结束时高度
    },
    onEnd: function(){ //结束回调
      $(".msg").fadeIn().animate({width: '250px'}, 500).fadeOut(3000).animate({width: '0px'}, 500); //提示信息
      fly.css("cursor","pointer").bind('click');
      $('.u-flyer').remove(); //移除dom
    },
    autoPlay: true, //是否直接运动,默认true
    speed: 1.0, //越大越快，默认1.2
    vertex_Rtop: 30, //运动轨迹最高点top值，默认20
  });
}

function showMsg(time=500) {
  $(".msg").fadeIn().animate({width: '250px'}, time).fadeOut(3000).animate({width: '0px'}, time); //提示信息
}

export {
  fly,
  showMsg,
}
