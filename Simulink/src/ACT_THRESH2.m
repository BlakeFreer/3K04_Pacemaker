classdef ACT_THRESH < Simulink.IntEnumType
    enumeration
        VLOW(0)
        LOW(1)
        MEDLOW(2)
        MED(3)
        MEDHIGH(4)
        HIGH(5)
        VHIGH(6)
    end
    methods (Static)
        function retVal = getDefaultValue()
            retVal = MODE.enum1;
        end
    end
end

