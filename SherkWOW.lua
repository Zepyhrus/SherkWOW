local zone = nil
local TimeSinceLastUpdate = 0

-- SLASH_TEST = "/test"
-- SlashCmdList["TEST"] = function(msg)
--    print("Hello World!")
-- end 

-- local btn = CreateFrame("Button", "myButton", UIParent, "SecureActionButtonTemplate")
-- btn:SetAttribute("type", "action")
-- btn:SetAttribute("action", 1)

local function UpdatSherkWOW(self, elapsed)
  if zone ~= GetRealZoneText() then
	  zone = GetRealZoneText()
  	SetMapToCurrentZone()
  end
  
  TimeSinceLastUpdate = TimeSinceLastUpdate + elapsed
 	
  if TimeSinceLastUpdate > .5 then	
    TimeSinceLastUpdate = 0
    local posX, posY = GetPlayerMapPosition("player");
    local x = math.floor(posX * 10000)/100;
    local y = math.floor(posY * 10000)/100;

    local base, posBuff, negBuff = UnitAttackPower("player");
    local effective = math.floor((base + posBuff + negBuff));

    -- local mainSpeed, offSpeed = UnitAttackSpeed("player");
    -- mainSpeed = math.floor(mainSpeed*100);
    
    SherkWOWFontString:SetText("|cffffffff"..effective.."")

    -- print(""..x..", "..y.."") 
 	end	
end
 
function SherkWOW_OnLoad(self, event,...) 
  self:RegisterEvent("ADDON_LOADED")	
end

function SherkWOW_OnEvent(self, event, ...) 
  -- 加载时创建窗口、
  if event == "ADDON_LOADED" and ... == "SherkWOW" then
    self:UnregisterEvent("ADDON_LOADED")		
    SherkWOW:SetSize(200, 500)
    SherkWOW:SetPoint("CENTER", 0, 0)
    SherkWOW:SetScript("OnUpdate", UpdatSherkWOW)

    local coordsFont = SherkWOW:CreateFontString("SherkWOWFontString", "ARTWORK", "GameFontNormal")
    -- local Path, Size, Flags = coordsFont:GetFont()
    -- coordsFont:SetFont(Path, 18, Flags)
    coordsFont:SetPoint("CENTER", "SherkWOW", 0, -60)
    -- coordsFont:SetJustifyH("CENTER")
    -- coordsFont:SetJustifyH("MIDDLE")

    coordsFont:Show()
    SherkWOW:Show()		
  end
end