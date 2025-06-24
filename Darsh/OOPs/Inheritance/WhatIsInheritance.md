#### What is inheritance?
- A class is the structure or blueprint of an object
  - if we are making a chair, class defines what features and components/ attributes of a chair are
- and an object is the physical implementation of the structure defined in the class
  - if you put all the features and component/attributes of a chair physically together, it will make a real chair


##### Let's understand with example 
- What are the basic features of a chair?
```
Class BasicChair:
    1. The material—Wood, metal, plastic
    2. Capacity 
    3. Color
    4. Legs
    5. Height
    6. Width
    7. Weight
    8. Handles - boolean field
    
```

```
Different type of chair -
class Office Mesh chair <- BasicChair
   2. Wheels
   3. Springs
   4. Mesh and back suport
   5. etc.
2. Gaming chair         <- BasicChair
   2. Wheels
   3. Springs
   4. Mesh and back suport
   5. does have table attached?  - boolean field
3. Sofa                  <- BasicChair
4. Beach chair           <- BasicChair
```