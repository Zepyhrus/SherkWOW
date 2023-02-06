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
    local posX, posY = GetPlayerMapPosition("player");
    local x = math.floor(posX * 10000)/100
    local y = math.floor(posY * 10000)/100
    SherkWOWFontString:SetText("|c98FB98ff("..x..", "..y..")")

  -- ConsoleExec("/cast Blood Boil");
    -- print('Hello world!');
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