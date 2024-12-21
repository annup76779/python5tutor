```
todo_app/
│
├── data/                     # Persistent storage
│   ├── tasks.json            # Main file storing tasks in JSON format
│   └── backup/               # Backup folder for storing older task files
│       ├── tasks_backup1.json
│       └── tasks_backup2.json
│
├── core/                     # Core application logic
│   ├── task_manager.py       # Functions for task CRUD operations
│   ├── storage_handler.py    # Functions for reading/writing data to files
|   ├── enums.py              # creating fixed data for the application
│   └── utilities.py          # Helper functions (sorting, filtering, etc.)
│
├── services/                 # Business logic layer
│   ├── task_service.py       # Combines core functions for business rules
│
├── tests/                    # Test cases for functional modules
│   ├── test_task_manager.py  # Test cases for task management functions
│   ├── test_storage.py       # Test cases for file handling functions
│   └── test_utilities.py     # Test cases for utility functions
│
├── logs/                     # Application logs
│   ├── app.log               # Log file for error/debug info
│
├── main.py                   # Entry point for the console app
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

#### data management and saving 
- task id
- task title
- task description
- status
- priority
