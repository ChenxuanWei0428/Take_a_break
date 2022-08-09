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

console.log("test");

function get_counter(time) {
    // return a string that lower the second by one
    let hour = Number(time.slice(0,2));
    let minutes = Number(time.slice(3, 5));
    let second = Number(time.slice(6, 8))-1;
    if (second < 0){
        second = 59;
        minutes--;
    }
    
    if (minutes < 0) {
        minutes = 59;
        hour -= 1;
    }

    if (hour < 0) {
        return false;
    }
    hour_str = hour.toLocaleString("en-US", {
        minimumIntegerDigirts: 2,
        useGrouping: false,
    });
    minutes_str = minutes.toLocaleString("en-US", {
        minimumIntegerDigirts: 2,
        useGrouping: false,
    });
    second_str = second.toLocaleString("en-US", {
        minimumIntegerDigirts: 2,
        useGrouping: false,
    });
    console.log(hour_str+":"+minutes_str+":"+second_str);
    return hour_str+":"+minutes_str+":"+second_str;
}