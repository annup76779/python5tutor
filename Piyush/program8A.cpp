// g++ thread.cpp -o a1.out -pthread

#include <iostream>
#include <thread>
#include <mutex>
#include<sstream>

using namespace std;

std::mutex show_mutex_g;
int first_timer_duration = 5;
int second_timer_duration = 10;


string get_thread_id(){
    /*
        This functions finds and return an ID of 
        the thread inside which this functions
        is called in string format.
    */
    show_mutex_g.lock();
    // getting the threadID in integer format.
    std::thread::id id0 = std::this_thread::get_id();
    show_mutex_g.unlock();
    std::stringstream oss;
    oss<<id0; // converting to string.
    return oss.str();
}


/*  
    timer1 function with duration taken from
    first_timer_duration global variable.
*/
void timer1(){
    // 
    string threadId = get_thread_id();
    cout<<"Thread1: "<<threadId<<" started"<<endl;
    std:this_thread::sleep_for(std::chrono::seconds(first_timer_duration));
    cout<<"Thread2: "<<threadId<<" ended"<<endl;
}


/*  
    timer1 function with duration taken from
    second_timer_duration global variable.
*/
void timer2(){
    string threadId = get_thread_id();
    cout<<"Thread2: "<<threadId<<" started"<<endl;
    std:this_thread::sleep_for(std::chrono::seconds(second_timer_duration));
    cout<<"Thread2: "<<threadId<<" ended"<<endl;
}


int main(){
    string main_thread_id = get_thread_id();

    cout<<"Main Thread: "<<main_thread_id<<" started"<<endl;
    std::thread t1(timer1);
    std::thread t2(timer2);
    t1.join();
    t2.join();
    cout<<"Main Thread: "<<main_thread_id<<" ended"<<endl;
    return 0;
}

/*
Expected OUTPUT -
---------------------

Main Thread: 139804606424896 started
Thread1: 139804606420736 started
Thread2: 139804598028032 started
Thread2: 139804606420736 ended
Thread2: 139804598028032 ended
Main Thread: 139804606424896 ended
*/

// Explaination of what happened
/*
The main thread started and then it initialized two timer threads
namely timer1 and timer2 of 5 and 10 second duration respectively.

Both the threads will start almost at exact time but the ending took time.
The timer1 thread ended in first 5 seconds of execution, although the timer2 
thread was initiated in the program after the timer1 thread but the timer2 
thread also ended first 10 seconds of execution of main thread.

Thus we saved 5 seconds of execution time of the complete program.
this is the benifit of using threads in programs.
*/
