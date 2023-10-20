<?php
    header('Content-Type: application/xml; charset=utf-8'); 
    require_once('apiClient.php');
    
    $realm                = $_GET['r'];
    $character            = $_GET['n'];
    $client               = new ApiClient ();
    $response             = $client->getCharacterModelData($realm, $character);
    $character_model_data = $response['response']['character_model_data'];
    $textures             = $response['response']['textures'];
    $attachments          = $response['response']['attachments'];
    $subtextures          = $response['response']['subtextures'];
    $animations           = $response['response']['animations'];
            
?>
<page globalSearch="1" lang="en" requestUrl="character-model.xml">
	<tabInfo tab="character" tabGroup="character" />
	<character owned="0">
	<models>
		<?php print '<model baseY="1.15" facedY="2.0" hideCape="'. $character_model_data['hide_cloak'] .'" hideHelm="'. $character_model_data['hide_helm'] . ' " id="1" 
		       modelFile="' . $character_model_data['CharacterBaseModel'] . '.m2" name="base" scale="1.25" skinFile="' . $character_model_data['CharacterBaseModel'] . '00.skin">' ?>
		<components>
			<?php print $character_model_data['components']; ?>
		</components>
		<textures>
		  <?php print '<texture file="'. $character_model_data['model']['baseSkin_texture_0'] .'" id="1">' ?>
			<?php print '<subTexture file="'. $character_model_data['model']['face_texture_1'] .'" h="0.125" w="0.5" x="0.0" y="0.625"/>' ?>
			
			<?php if (!$character_model_data['gender_id'] && $character_model_data['model']['facialhr_texture_1'] != "") { ?>
				<?php print '<subTexture file="'. $character_model_data['model']['facialhr_texture_1'] .'" h="0.125" w="0.5" x="0.0" y="0.625"/>' ?>
			<?php } ?>
			
			<?php print '<subTexture file="' . $character_model_data['model']['face_texture_0'] .'" h="0.25" w="0.5" x="0.0" y="0.75"/>' ?>
			
			<?php if (!$character_model_data['gender_id']) { ?>
				<?php print '<subTexture file="' . $character_model_data['model']['facialhr_texture_0'] . '" h="0.25" w="0.5" x="0.0" y="0.75" />' ?>
			<?php } ?>
			
			<?php print $subtextures ?>
		  </texture>
		  <?php print '<texture file="' . $character_model_data['model']['hair_texture_0'] . ' " id="6" />' ?>
		  <?php print $textures ?>
		</textures>
		<?php print $attachments ?>
		<animations>
			<?php print $animations ?>
			<animation id="69" key="dance" weapons="no"/>
			<animation id="70" key="laugh" weapons="no"/>
			<animation id="82" key="flex" weapons="no"/>
			<animation id="78" key="chicken" weapons="no"/>
			<animation id="120" key="crouch" weapons="no"/>
			<animation id="60" key="talk" weapons="no"/>
			<animation id="66" key="bow" weapons="no"/>
			<animation id="67" key="wave" weapons="no"/>
			<animation id="73" key="rude" weapons="no"/>
			<animation id="76" key="kiss" weapons="no"/>
			<animation id="77" key="cry" weapons="no"/>
			<animation id="84" key="point" weapons="no"/>
			<animation id="113" key="salute" weapons="no"/>
			<animation id="185" key="yes" weapons="no"/>
			<animation id="186" key="no" weapons="no"/>
			<animation id="195" key="train" weapons="no"/>
		</animations>
	  </model>
	</models>
	<backgrounds>
		<background file="bgs/full/dalaran" key="dalaran" scale="2.8" x="0" y="155"/>
		<background file="bgs/full/deathknight" key="deathknight" scale="3.0" x="0" y="145"/>
		<background file="bgs/full/nightelf" key="nightelf" scale="3.15" x="0" y="165"/>
		<background file="bgs/full/argenttournament" key="argenttournament" scale="2.8" x="0" y="155"/>
		<background file="bgs/full/shattrath" key="shattrath" scale="2.8" x="0" y="155"/>
		<background file="bgs/full/shattrath2" key="shattrath2" scale="2.8" x="0" y="155"/>
		<background file="bgs/full/wintergrasp" key="wintergrasp" scale="2.8" x="0" y="155"/>
		<background file="bgs/full/alteracvalley_horde" key="alteracvalley_horde" scale="2.8" x="0" y="155"/>
		<background file="bgs/full/alteracvalley_alliance" key="alteracvalley_alliance" scale="2.8" x="0" y="155"/>
	</backgrounds>
	</character>
</page>