classdef MODE < Simulink.IntEnumType
    enumeration
        Off(0)
        DDD(1)
        VDD(2)
        DDI(3)
        DOO(4)
        AOO(5)
        AAI(6)
        VOO(7)
        VVI(8)
        AAT(9)
        VVT(10)
    end
    methods (Static)
        function retVal = getDefaultValue()
            retVal = MODE.Off;
        end
    end
end