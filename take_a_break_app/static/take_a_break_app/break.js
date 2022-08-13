function time_after_redirect(time) {
    target_url = "http://"+window.location.host+"/main";
    break_time = get_total_second(time);

    var noti = setTimeout(function() {
        notify()
    }, break_time*1000);

    jump_time = break_time+5;
    
    var timer = setTimeout(function() {
        window.location.href=target_url;
    }, jump_time*1000);
    
}

function get_total_second(time) {
    // time should be in format of hh:mm:ss
    return Number(time.slice(0,2))*3600+Number(time.slice(3, 5))*60+Number(time.slice(6, 8));
}

function jump_link(link) {

}

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
        minimumIntegerDigits: 2,
        useGrouping: false,
    });
    minutes_str = minutes.toLocaleString("en-US", {
        minimumIntegerDigits: 2,
        useGrouping: false,
    });
    second_str = second.toLocaleString("en-US", {
        minimumIntegerDigits: 2,
        useGrouping: false,
    });
    return hour_str+":"+minutes_str+":"+second_str;
    
}

function open_in_new_tab(url) {
    var win = window.open(url, '_blank');
    win.focus();
}

function notify() {
    if (Notification.permission !== 'granted')
        Notification.requestPermission();
    else {
        let notification = new Notification('Notification title', {
            body: "Your break time is up!",
        });
        //window.open('http://127.0.0.1:8000/main');
    }
}
   
