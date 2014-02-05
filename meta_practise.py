class C():

    class mclass(type):
        def __new__(mcs, name, bases, attributes):
            # Do something clever with name, base or attributes
            name="so_cool "+name
            cls = type.__new__(mcs, name, bases, attributes)
            # Do something cleverer with the class itself
            print ("I've created class whose","name: ",name," mcs: ",mcs," bases: ",bases," attributes: ",attributes)
            return cls

    class A(object):
        "Customizing the creation of class A"
        __metaclass__=C.mclass

    class B(A):
        static = 1
