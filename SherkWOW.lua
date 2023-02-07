local zone = nil
local TimeSinceLastUpdate = 0

SLASH_TEST = "/test"
SlashCmdList["TEST"] = function(msg)
   print("Hello World!")
end 

local btn = CreateFrame("Button", "myButton", UIParent, "SecureActionButtonTemplate")
btn:SetAttribute("type", "action")
btn:SetAttribute("action", 1)

local function UpdatSherkWOW(self, elapsed)
  if zone ~= GetRealZoneText() then
	  zone = GetRealZoneText()
  	SetMapToCurrentZone()
  end
  
  TimeSinceLastUpdate = TimeSinceLastUpdate + elapsed
 	
  if TimeSinceLastUpdate > .5 then	
    TimeSinceLastUpdate = 0
    -- local posX, posY = GetPlayerMapPosition("player");
    -- local x = math.floor(posX * 10000)/100
    -- local y = math.floor(posY * 10000)/100

    local base, posBuff, negBuff = UnitAttackPower("player");
    local effective = math.floor((base + posBuff + negBuff) / 1000);
    
    SherkWOWFontString:SetText("[  "..effective.."  ]")

    -- print("Attack power: "..effective.."...");
    -- D:\Installation\World of Warcraft 5.4.8\Interface\AddOns\SherkWOW\SherkWOW.lua
 	end	
end
 
function SherkWOW_OnLoad(self, event,...) 
  self:RegisterEvent("ADDON_LOADED")	
end

function SherkWOW_OnEvent(self, event, ...) 
  if event == "ADDON_LOADED" and ... == "SherkWOW" then
    self:UnregisterEvent("ADDON_LOADED")		
    SherkWOW:SetSize(100, 50)
    SherkWOW:SetPoint("TOP", "Minimap", "BOTTOM", 5, -5)
    SherkWOW:SetScript("OnUpdate", UpdatSherkWOW)
    local coordsFont =    SherkWOW:CreateFontString("SherkWOWFontString", "ARTWORK", "GameFontNormal")
    coordsFont:SetPoint("CENTER", "SherkWOW", "CENTER", 0, 0)
    coordsFont:Show()
    SherkWOW:Show()		
  end
end