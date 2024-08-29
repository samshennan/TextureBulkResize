bl_info = {
    "name": "Texture Resizer",
    "description": "Adds a button to resize all textures in the project and save them.",
    "author": "Sam Shennan",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Texture Resizer",
    "category": "Texture"
}

import bpy
from bpy_extras.io_utils import ExportHelper

class TextureResizerPanel(bpy.types.Panel):
    bl_label = "Texture Resizer"
    bl_idname = "VIEW3D_PT_texture_resizer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Texture'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Downscale all image textures in the current Blender project down to:")

        row = layout.row()
        col = row.column()
        col.operator("texture.resize_all", text="4K - 4096px").image_resolution = "4096"
        col.operator("texture.resize_all", text="2K - 2048px").image_resolution = "2048"
        col.operator("texture.resize_all", text="1K - 1024px").image_resolution = "1024"
        col.operator("texture.resize_all", text="512px").image_resolution = "512"
        col.operator("texture.resize_all", text="256px").image_resolution = "256"

        row = layout.row()
        row.operator("image.save_all", text="Save All Textures")

        row = layout.row()
        row.operator("export_all_textures.save_as", text="Export All Textures")

class ResizeAllTexturesOperator(bpy.types.Operator):
    bl_idname = "texture.resize_all"
    bl_label = "Resize All Textures"

    image_resolution: bpy.props.StringProperty()

    def execute(self, context):
        for img in bpy.data.images:
            if img.size[0] > int(self.image_resolution) or img.size[1] > int(self.image_resolution):
                img.scale(int(self.image_resolution), int(self.image_resolution))
        return {'FINISHED'}

class SaveAllTexturesOperator(bpy.types.Operator):
    bl_idname = "image.save_all"
    bl_label = "Save All Textures"

    def execute(self, context):
        #for img in bpy.data.images:
        #if img.is_dirty:
        #img.save_render(filepath=img.filepath)
        bpy.ops.image.save_all_modified()
        return {'FINISHED'}


class ExportAllTexturesOperator(bpy.types.Operator, ExportHelper):
    bl_idname = "export_all_textures.save_as"
    bl_label = "Export All Textures"

    filename_ext = ".png"

    def execute(self, context):
        for img in bpy.data.images:
            filepath = self.filepath.replace(".png", f"_{img.name}.png")
            img.save_render(filepath)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(TextureResizerPanel)
    bpy.utils.register_class(ResizeAllTexturesOperator)
    bpy.utils.register_class(SaveAllTexturesOperator)
    bpy.utils.register_class(ExportAllTexturesOperator)

def unregister():
    bpy.utils.unregister_class(TextureResizerPanel)
    bpy.utils.unregister_class(ResizeAllTexturesOperator)
    bpy.utils.unregister_class(SaveAllTexturesOperator)
    bpy.utils.unregister_class(ExportAllTexturesOperator)

if __name__ == "__main__":
    register()
