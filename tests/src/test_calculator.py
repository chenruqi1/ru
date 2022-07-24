from app.src.calculator import Calculator

cal=Calculator()

def test_add():
    assert cal.add(1,1)==2
    assert cal.add(1,2)==3

def test_substract():
<<<<<<< HEAD
    assert cal.add(3,1)==2

=======
    assert cal.add(2,1)==1
>>>>>>> ae18af87e8547f63fcda9187d14201b5ecdc2be2
