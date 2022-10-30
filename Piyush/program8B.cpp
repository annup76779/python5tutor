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
    cout<<"Thread1: "<<threadId<<" ended"<<endl;
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

void handle_thread(){
    std::thread t1(timer1);
    std::thread t2(timer2);
    t1.detach();
    t2.detach();
}


int main(){
    string main_thread_id = get_thread_id();

    cout<<"Main Thread: "<<main_thread_id<<" started"<<endl;
    /*
    function that creates and detaches the timer threads as 
    specified in the B part of the question.
    */
    handle_thread();
    cout<<"Main Thread: "<<main_thread_id<<" ended"<<endl;
    return 0;
}

/*
one of the lot different OUTPUTs -
----------------------------------

Main Thread: 139814528345920 started
Thread1: 139814528341760 started
Main Thread: 139814528345920 ended
Thread2: 139814519949056 started
*/

// Explaination of what happened
/*
The main thread started and then it initialized two timer threads
namely timer1 and timer2 of 5 and 10 second duration respectively.

But since both the threads were detached from the main thread
their execution will start but the main thread will end even before the completion
of the timer threads. But the part of the threads that was already executed while
the execution of main thread will be shown on console if we print it.
*/
