function time_after_redirect(time) {
    target_url = "http://"+window.location.host+"/main";
    break_time = get_total_second(time);
    console.log(break_time);
    console.log(target_url);
    
    var timer = setTimeout(function() {
        window.location.href=target_url;
    }, break_time*1000);
    
}

function get_total_second(time) {
    // time should be in format of hh:mm:ss
    return Number(time.slice(0,2))*3600+Number(time.slice(3, 5))*60+Number(time.slice(6, 8));
}

function jump_link(link) {

}

function counter(time) {
    // return a string that lower the second by one
    hour = Number(time.slice(0,2));
    minutes = Number(time.slice(3, 5));
    second = Number(time.slice(6, 8))-1;
    if (second < 0){
        second = 59;
        minutes--;
    }
    if (minutes < 0) {
        minutes = 59;
        hours -= 1;
    }
    if (hours < 0) {
        
    }
}